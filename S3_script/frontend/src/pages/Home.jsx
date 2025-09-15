import { useState, useEffect } from "react";
import api from "../api";
import { Link } from "react-router-dom";

export default function Home() {
  const [students, setStudents] = useState([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
    fetchStudents();
  }, []);

  const fetchStudents = async () => {
    const res = await api.get("/students");
    setStudents(res.data);
  };

  const addStudent = async (e) => {
    e.preventDefault();
    await api.post("/students", { name, email });
    setName("");
    setEmail("");
    fetchStudents();
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Student Management</h1>

      {/* Add Student Form */}
      <form onSubmit={addStudent} className="mb-6 flex gap-2">
        <input
          type="text"
          placeholder="Name"
          className="border p-2"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="email"
          placeholder="Email"
          className="border p-2"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <button className="bg-blue-500 text-white px-4 py-2">Add</button>
      </form>

      {/* Student Table */}
      <table className="w-full border">
        <thead>
          <tr className="bg-gray-100">
            <th className="border p-2">ID</th>
            <th className="border p-2">Name</th>
            <th className="border p-2">Email</th>
            <th className="border p-2">Actions</th>
          </tr>
        </thead>
        <tbody>
          {students.map((s) => (
            <tr key={s.id}>
              <td className="border p-2">{s.id}</td>
              <td className="border p-2">{s.name}</td>
              <td className="border p-2">{s.email}</td>
              <td className="border p-2">
                <Link
                  to={`/edit/${s.id}`}
                  className="bg-yellow-400 px-3 py-1 mr-2"
                >
                  Edit
                </Link>
                <button
                  onClick={async () => {
                    await api.delete(`/students/${s.id}`);
                    fetchStudents();
                  }}
                  className="bg-red-500 text-white px-3 py-1"
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
