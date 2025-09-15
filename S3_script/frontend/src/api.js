import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:5000/api", // change to your backend base URL
});
