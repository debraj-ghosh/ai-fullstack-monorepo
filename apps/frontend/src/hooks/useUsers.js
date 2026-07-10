import { useEffect, useState } from "react";
import {
    getUsers,
    createUser,
    updateUser,
    deleteUser,
} from "../services/userService";

export function useUsers() {

    const [users, setUsers] = useState([]);

    const loadUsers = async () => {
        try {
            const data = await getUsers();
            setUsers(data);
        } catch (error) {
            console.error("Failed to load users:", error);
        }
    };

    useEffect(() => {
        let isMounted = true;
        
        const load = async () => {
            try {
                const data = await getUsers();
                if (isMounted) {
                    setUsers(data);
                }
            } catch (error) {
                console.error("Failed to load users:", error);
            }
        };
        
        load();
        
        return () => {
            isMounted = false;
        };
    }, []);

    const addUser = async (user) => {
        await createUser(user);
        await loadUsers();
    };

    const editUser = async (id, user) => {
        await updateUser(id, user);
        await loadUsers();
    };

    const removeUser = async (id) => {
        await deleteUser(id);
        await loadUsers();
    };

    return {
        users,
        addUser,
        editUser,
        removeUser,
    };
}