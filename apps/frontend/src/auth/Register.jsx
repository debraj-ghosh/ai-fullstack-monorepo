import { useState } from "react";
import { registerUser } from "../api/authApi";

function Register() {

    const [form, setForm] = useState({
        first_name: "",
        last_name: "",
        email: "",
        password: "",
    });

    const handleSubmit = async (e) => {

        e.preventDefault();

        await registerUser(form);

        alert("Registration Successful");
    };

    return (

        <form onSubmit={handleSubmit}>

            <h2>Register</h2>

            <input
                placeholder="First Name"
                onChange={(e) =>
                    setForm({
                        ...form,
                        first_name: e.target.value,
                    })
                }
            />

            <input
                placeholder="Last Name"
                onChange={(e) =>
                    setForm({
                        ...form,
                        last_name: e.target.value,
                    })
                }
            />

            <input
                placeholder="Email"
                onChange={(e) =>
                    setForm({
                        ...form,
                        email: e.target.value,
                    })
                }
            />

            <input
                type="password"
                placeholder="Password"
                onChange={(e) =>
                    setForm({
                        ...form,
                        password: e.target.value,
                    })
                }
            />

            <button>

                Register

            </button>

        </form>
    );
}

export default Register;