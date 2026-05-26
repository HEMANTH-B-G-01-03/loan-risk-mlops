import { useState } from "react";
import axios from "axios";

function App() {

  const [formData, setFormData] = useState({
    loan_amnt: "",
    term: "",
    int_rate: "",
    installment: "",
    grade: "",
    sub_grade: "",
    emp_length: "",
    home_ownership: "",
    annual_inc: "",
    verification_status: "",
    purpose: "",
    dti: "",
    delinq_2yrs: "",
    fico_range_low: "",
    inq_last_6mths: "",
    open_acc: "",
    pub_rec: "",
    revol_bal: "",
    revol_util: "",
    total_acc: "",
    application_type: ""
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: Number(e.target.value)
    });
  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/predict",
        formData
      );

      setResult(response.data);

    } catch (error) {

      console.error(error);

      alert("Prediction failed");
    }
  };

  return (

    <div className="min-h-screen bg-gray-100 p-8">

      <h1 className="text-4xl font-bold text-center mb-8 text-blue-700">
        Loan Risk Prediction System
      </h1>

      <div className="max-w-5xl mx-auto grid md:grid-cols-2 gap-8">

        {/* FORM SECTION */}

        <form
          onSubmit={handleSubmit}
          className="bg-white p-6 rounded-2xl shadow-lg"
        >

          <h2 className="text-2xl font-semibold mb-4">
            Enter Loan Details
          </h2>

          <div className="grid grid-cols-2 gap-4">

            {Object.keys(formData).map((key) => (

              <input
                key={key}
                type="number"
                step="any"
                name={key}
                placeholder={key}
                onChange={handleChange}
                className="border p-3 rounded-lg"
                required
              />
            ))}

          </div>

          <button
            type="submit"
            className="mt-6 w-full bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-xl font-semibold"
          >
            Predict Loan Risk
          </button>

        </form>

        {/* RESULT SECTION */}

        <div className="bg-white p-6 rounded-2xl shadow-lg flex flex-col justify-center">

          <h2 className="text-2xl font-semibold mb-4">
            Prediction Result
          </h2>

          {result ? (

            <div className="space-y-4">

              <div className="text-xl">
                <span className="font-bold">Prediction:</span>{" "}
                {result.risk_label}
              </div>

              <div className="text-xl">
                <span className="font-bold">
                  Default Probability:
                </span>{" "}
                {(result.default_probability * 100).toFixed(2)}%
              </div>

              <div
                className={`p-4 rounded-xl text-white text-center font-bold text-xl ${
                  result.prediction === 1
                    ? "bg-red-500"
                    : "bg-green-500"
                }`}
              >
                {result.prediction === 1
                  ? "HIGH RISK"
                  : "SAFE CUSTOMER"}
              </div>

            </div>

          ) : (

            <p className="text-gray-500">
              No prediction yet
            </p>

          )}

        </div>

      </div>

    </div>
  );
}

export default App;