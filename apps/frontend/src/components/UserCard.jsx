function UserCard({ user, onDelete, onEdit }) {

    return (
        <div
            style={{
                border: "1px solid gray",
                marginBottom: "10px",
                padding: "10px",
            }}
        >
            <h3>
                {user.first_name} {user.last_name}
            </h3>

            <p>{user.email}</p>

            <button onClick={() => onDelete(user.id)}>
                Delete
            </button>

            <button
                onClick={() => onEdit && onEdit(user)}
                style={{ marginLeft: "8px" }}
            >
                Update
            </button>
        </div>
    );
}

export default UserCard;