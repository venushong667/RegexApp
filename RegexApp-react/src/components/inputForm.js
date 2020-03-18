import React from "react";
import { useForm } from "react-hook-form";

const InputForm = ({ onSubmit, result }) => {
  const { register, handleSubmit } = useForm({});

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input name="input1" placeholder="Input1" ref={register} />
      <br />
      <input name="input2" placeholder="Input2" ref={register} />
      <br />
      <input value={result} placeholder="Result" disabled />
      <br />
      <button type="submit">Submit</button>
    </form>
  );
};

export default InputForm;
