import UserCard from "./UserCard";

function UserList({ users, onDelete, onEdit }) {
    return (
        <>
            <h2>Users</h2>

            {users.map((user) => (
                <UserCard
                    key={user.id}
                    user={user}
                    onDelete={onDelete}
                    onEdit={onEdit}
                />
            ))}
        </>
    );
}

export default UserList;