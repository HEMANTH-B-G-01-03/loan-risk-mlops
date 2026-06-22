// import { useState } from "react";
// import axios from "axios";

// function App() {

//   const [formData, setFormData] = useState({
//     loan_amnt: "",
//     term: "",
//     int_rate: "",
//     installment: "",
//     grade: "",
//     sub_grade: "",
//     emp_length: "",
//     home_ownership: "",
//     annual_inc: "",
//     verification_status: "",
//     purpose: "",
//     dti: "",
//     delinq_2yrs: "",
//     fico_range_low: "",
//     inq_last_6mths: "",
//     open_acc: "",
//     pub_rec: "",
//     revol_bal: "",
//     revol_util: "",
//     total_acc: "",
//     application_type: ""
//   });

//   const [result, setResult] = useState(null);

//   const handleChange = (e) => {

//     setFormData({
//       ...formData,
//       [e.target.name]: Number(e.target.value)
//     });
//   };

//   const handleSubmit = async (e) => {

//     e.preventDefault();

//     try {

//       const response = await axios.post(
//         "http://127.0.0.1:8000/predict",
//         formData
//       );

//       setResult(response.data);

//     } catch (error) {

//       console.error(error);

//       alert("Prediction failed");
//     }
//   };

//   return (

//     <div className="min-h-screen bg-gray-100 p-8">

//       <h1 className="text-4xl font-bold text-center mb-8 text-blue-700">
//         Loan Risk Prediction System
//       </h1>

//       <div className="max-w-5xl mx-auto grid md:grid-cols-2 gap-8">

//         {/* FORM SECTION */}

//         <form
//           onSubmit={handleSubmit}
//           className="bg-white p-6 rounded-2xl shadow-lg"
//         >

//           <h2 className="text-2xl font-semibold mb-4">
//             Enter Loan Details
//           </h2>

//           <div className="grid grid-cols-2 gap-4">

//             {Object.keys(formData).map((key) => (

//               <input
//                 key={key}
//                 type="number"
//                 step="any"
//                 name={key}
//                 placeholder={key}
//                 onChange={handleChange}
//                 className="border p-3 rounded-lg"
//                 required
//               />
//             ))}

//           </div>

//           <button
//             type="submit"
//             className="mt-6 w-full bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-xl font-semibold"
//           >
//             Predict Loan Risk
//           </button>

//         </form>

//         {/* RESULT SECTION */}

//         <div className="bg-white p-6 rounded-2xl shadow-lg flex flex-col justify-center">

//           <h2 className="text-2xl font-semibold mb-4">
//             Prediction Result
//           </h2>

//           {result ? (

//             <div className="space-y-4">

//               <div className="text-xl">
//                 <span className="font-bold">Prediction:</span>{" "}
//                 {result.risk_label}
//               </div>

//               <div className="text-xl">
//                 <span className="font-bold">
//                   Default Probability:
//                 </span>{" "}
//                 {(result.default_probability * 100).toFixed(2)}%
//               </div>

//               <div
//                 className={`p-4 rounded-xl text-white text-center font-bold text-xl ${
//                   result.prediction === 1
//                     ? "bg-red-500"
//                     : "bg-green-500"
//                 }`}
//               >
//                 {result.prediction === 1
//                   ? "HIGH RISK"
//                   : "SAFE CUSTOMER"}
//               </div>

//             </div>

//           ) : (

//             <p className="text-gray-500">
//               No prediction yet
//             </p>

//           )}

//         </div>

//       </div>

//     </div>
//   );
// }

// export default App;




import { useState } from "react";
import axios from "axios";

function App() {

  const [formData, setFormData] = useState({
    loan_amnt: "",
    annual_inc: "",
    int_rate: "",
    emp_length: "",
    fico_range_low: "",
    dti: "",
    open_acc: ""
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

    // Hidden/default values
    const finalData = {

      loan_amnt: formData.loan_amnt,
      annual_inc: formData.annual_inc,
      int_rate: formData.int_rate,
      emp_length: formData.emp_length,
      fico_range_low: formData.fico_range_low,
      dti: formData.dti,
      open_acc: formData.open_acc,

      // Default internal values
      term: 1,
      installment: 350,
      grade: 2,
      sub_grade: 5,
      home_ownership: 1,
      verification_status: 1,
      purpose: 3,
      delinq_2yrs: 0,
      inq_last_6mths: 1,
      pub_rec: 0,
      revol_bal: 12000,
      revol_util: 45.5,
      total_acc: 20,
      application_type: 0
    };

    try {

      const response = await axios.post(
        "http://32.199.138.117:8000/predict" , 
        finalData
      );

      setResult(response.data);

    } catch (error) {

      console.error(error);

      alert("Prediction failed");
    }
  };

  return (

    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-indigo-200 p-8">

      <h1 className="text-5xl font-bold text-center text-blue-800 mb-10">
        Loan Risk Prediction System
      </h1>

      <div className="max-w-5xl mx-auto grid md:grid-cols-2 gap-10">

        {/* FORM CARD */}

        <div className="bg-white p-8 rounded-3xl shadow-2xl">

          <h2 className="text-3xl font-semibold mb-6 text-gray-800">
            Enter Loan Details
          </h2>

          <form
            onSubmit={handleSubmit}
            className="space-y-5"
          >

            <input
              type="number"
              name="loan_amnt"
              placeholder="Loan Amount"
              onChange={handleChange}
              className="w-full p-4 border rounded-xl"
              required
            />

            <input
              type="number"
              name="annual_inc"
              placeholder="Annual Income"
              onChange={handleChange}
              className="w-full p-4 border rounded-xl"
              required
            />

            <input
              type="number"
              step="any"
              name="int_rate"
              placeholder="Interest Rate (%)"
              onChange={handleChange}
              className="w-full p-4 border rounded-xl"
              required
            />

            <input
              type="number"
              name="emp_length"
              placeholder="Employment Length (Years)"
              onChange={handleChange}
              className="w-full p-4 border rounded-xl"
              required
            />

            <input
              type="number"
              name="fico_range_low"
              placeholder="Credit Score"
              onChange={handleChange}
              className="w-full p-4 border rounded-xl"
              required
            />

            <input
              type="number"
              step="any"
              name="dti"
              placeholder="Debt-To-Income Ratio"
              onChange={handleChange}
              className="w-full p-4 border rounded-xl"
              required
            />

            <input
              type="number"
              name="open_acc"
              placeholder="Open Accounts"
              onChange={handleChange}
              className="w-full p-4 border rounded-xl"
              required
            />

            <button
              type="submit"
              className="w-full bg-blue-700 hover:bg-blue-800 text-white p-4 rounded-xl text-lg font-semibold transition"
            >
              Predict Loan Risk
            </button>

          </form>

        </div>

        {/* RESULT CARD */}

        <div className="bg-white p-8 rounded-3xl shadow-2xl flex flex-col justify-center">

          <h2 className="text-3xl font-semibold mb-6 text-gray-800">
            Prediction Result
          </h2>

          {result ? (

            <div className="space-y-6">

              <div className="text-2xl">
                <span className="font-bold">
                  Risk Status:
                </span>{" "}
                {result.risk_label}
              </div>

              <div className="text-2xl">
                <span className="font-bold">
                  Default Probability:
                </span>{" "}
                {(result.default_probability * 100).toFixed(2)}%
              </div>

              <div
                className={`p-6 rounded-2xl text-center text-white text-3xl font-bold ${
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

            <p className="text-gray-500 text-lg">
              Enter customer details to predict loan risk.
            </p>

          )}

        </div>

      </div>

    </div>
  );
}

export default App;