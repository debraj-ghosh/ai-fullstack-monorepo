from app.repositories.user_repository import UserRepository
from app.schemas import user

from app.cache.cache_service import CacheService

class UserService:

    def __init__(self):
        self.repository = UserRepository()
        self.cache = CacheService()

    def create_user(self, db, user):
        created = self.repository.create(
            db,
            user
        )
        self.cache.delete("users")
        return created

    def get_users(self, db):
        cache_key = "users"
        cached_users = self.cache.get(cache_key)
        if cached_users:
            print("Loaded Users from Redis")
            return cached_users
        users = self.repository.get_all(db)
        users_json = [
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            }
            for user in users
        ]
        self.cache.set(
            cache_key,
            users_json
        )
        print("Loaded Users from PostgreSQL")
        return users_json

    # def get_user(self, db, user_id):
    #     cache_key = f"user:{user_id}"
    #     cached_user = self.cache.get(cache_key)
    #     if cached_user:
    #         print("User Loaded From Redis")
    #         return cached_user
    #     user = self.repository.get_by_id(
    #         db,
    #         user_id
    #     )
    #     if user:
    #         self.cache.set(
    #             cache_key,
    #             {
    #                 "id": user.id,
    #                 "first_name": user.first_name,
    #                 "last_name": user.last_name,
    #                 "email": user.email,
    #             }
    #         )
    #         return {
    #             "id": user.id,
    #             "first_name": user.first_name,
    #             "last_name": user.last_name,
    #             "email": user.email,
    #         }
    #     return None
    def get_user(self, db, user_id):
        return self.repository.get_by_id(db, user_id)
    
    def get_user_cached(self, db, user_id):
        cache_key = f"user:{user_id}"
        cached_user = self.cache.get(cache_key)
        if cached_user:
            print("User Loaded From Redis")
            return cached_user
        user = self.repository.get_by_id(db, user_id)
        if not user:
            return None
        user_json = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }
        self.cache.set(cache_key, user_json)
        print("User Loaded From PostgreSQL")
        return user_json

    def delete_user(self, db, user):
        self.repository.delete(
            db,
            user
        )
        self.cache.delete("users")
        self.cache.delete(
            f"user:{user.id}"
        )
    
    def update_user(self, db, db_user, user):
        updated = self.repository.update(db, db_user, user)
        self.cache.delete("users")
        self.cache.delete(
            f"user:{updated.id}"
        )
        return updated