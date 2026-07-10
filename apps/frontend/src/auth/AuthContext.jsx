import { createContext, useContext, useState } from "react";
import {
    getToken,
    removeToken,
    saveToken,
} from "../utils/token";

const AuthContext = createContext();

export function AuthProvider({ children }) {

    const [token, setToken] = useState(getToken());

    const login = (jwtToken) => {

        saveToken(jwtToken);

        setToken(jwtToken);
    };

    const logout = () => {

        removeToken();

        setToken(null);
    };

    return (

        <AuthContext.Provider
            value={{
                token,
                login,
                logout,
                isAuthenticated: !!token,
            }}
        >

            {children}

        </AuthContext.Provider>
    );
}

export const useAuth = () => useContext(AuthContext);