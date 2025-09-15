import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import api from "../api";

export default function EditStudent() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
    api.get(`/students/${id}`).then((res) => {
      setName(res.data.name);
      setEmail(res.data.email);
    });
  }, [id]);

  const updateStudent = async (e) => {
    e.preventDefault();
    await api.put(`/students/${id}`, { name, email });
    navigate("/");
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Edit Student</h1>
      <form onSubmit={updateStudent} className="flex flex-col gap-4">
        <input
          type="text"
          className="border p-2"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="email"
          className="border p-2"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <button className="bg-green-500 text-white px-4 py-2">Update</button>
      </form>
    </div>
  );
}
