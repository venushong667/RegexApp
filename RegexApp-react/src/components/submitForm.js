import React from "react";
import InputForm from "./inputForm";
import { APIV1 } from "../api/api";

const SubmitForm = () => {
  const [state, setState] = React.useState({ result: "" });

  const { result } = state;

  const submitInput = values => {
    const apiV1 = APIV1();

    apiV1
      .postOutput(values)
      .then(async response => {
        const data = response.data;
        setState({ ...state, result: data.result });
        console.log(response);

        return data;
      })
      .catch(err => console.log(err));
  };

  return <InputForm onSubmit={submitInput} result={result} />;
};

export default SubmitForm;
