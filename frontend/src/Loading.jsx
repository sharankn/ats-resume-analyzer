import "./index.css";

function Loading() {
  return (
    <div className="container">
      <div className="card">
        <h1>Analyzing Resume...</h1>

        <div className="loader"></div>

        <p>Please wait while we compare your resume with the job description.</p>
      </div>
    </div>
  );
}

export default Loading;