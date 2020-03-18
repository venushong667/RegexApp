import axios from "axios";

export const APIV1 = (baseURL = "http://localhost:5010/api") => {
  const api = axios.create({
    baseURL,
    headers: {
      "Content-Type": "application/json"
    },
    withCredentials: true
  });

  const postOutput = values =>
    api.post(`/output`, {
      input1: values.input1,
      input2: values.input2
    });

  return { postOutput };
};
