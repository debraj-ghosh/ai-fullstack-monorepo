import { useState } from "react";

function UserForm({ onSubmit, initialData = null, submitLabel }) {

    const [form, setForm] = useState(() => ({
        first_name: (initialData && initialData.first_name) || "",
        last_name: (initialData && initialData.last_name) || "",
        email: (initialData && initialData.email) || "",
        password: "",
    }));

    // If parent intentionally changes initialData after mount, caller can reset
    // the form by providing a different key or by controlling externally.

    const handleChange = (e) => {

        setForm({
            ...form,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(form);
    };

    return (
        <form onSubmit={handleSubmit}>

            <input
                name="first_name"
                placeholder="First Name"
                value={form.first_name}
                onChange={handleChange}
            />

            <br /><br />

            <input
                name="last_name"
                placeholder="Last Name"
                value={form.last_name}
                onChange={handleChange}
            />

            <br /><br />

            <input
                name="email"
                placeholder="Email"
                value={form.email}
                onChange={handleChange}
            />

            <br /><br />

            <input
                name="password"
                placeholder="Password"
                type="password"
                value={form.password}
                onChange={handleChange}
            />

            <br /><br />

            <button type="submit">
                {submitLabel || "Add User"}
            </button>

            {initialData && (
                <button
                    type="button"
                    onClick={() => {
                        // reset to empty and allow parent to cancel edit by passing null
                        setForm({ first_name: "", last_name: "", email: "", password: "" });
                        if (typeof window !== "undefined" && window.__USER_FORM_CANCEL__) {
                            window.__USER_FORM_CANCEL__();
                        }
                    }}
                    style={{ marginLeft: "8px" }}
                >
                    Cancel
                </button>
            )}

        </form>
    );
}

export default UserForm;