import UserForm from "../components/UserForm";
import UserList from "../components/UserList";
import { useUsers } from "../hooks/useUsers";
import { useState, useEffect } from "react";

function Home() {

    const {
        users,
        addUser,
        editUser,
        removeUser,
    } = useUsers();

    const [editingUser, setEditingUser] = useState(null);

    useEffect(() => {
        // hook for the cancel button inside UserForm
        window.__USER_FORM_CANCEL__ = () => setEditingUser(null);
        return () => {
            window.__USER_FORM_CANCEL__ = undefined;
        };
    }, []);

    const handleEdit = (user) => {
        setEditingUser(user);
    };

    const handleSubmit = async (form) => {
        if (editingUser) {
            await editUser(editingUser.id, form);
            setEditingUser(null);
        } else {
            await addUser(form);
        }
    };

    return (
        <div style={{ padding: "40px" }}>

            <h1>User Management</h1>

            <UserForm
                onSubmit={handleSubmit}
                initialData={editingUser}
                submitLabel={editingUser ? "Update User" : "Add User"}
            />

            <hr />

            <UserList
                users={users}
                onDelete={removeUser}
                onEdit={handleEdit}
            />

        </div>
    );
}

export default Home;