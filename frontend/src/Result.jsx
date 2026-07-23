import "./index.css";

function Result({ result, onReset }) {
  if (!result) {
    return null;
  }

  return (
    <div className="container">
      <div className="card">
        <h1>AI ATS Resume Analyzer</h1>

        {/* Score */}
        <div className="score">
          {result.score}%
        </div>

        {/* Matching Skills */}
        <h2>Matching Skills</h2>

        <div className="skills">
          {result.matching_skills.map((skill, index) => (
            <span key={index} className="good">
              {skill}
            </span>
          ))}
        </div>

        {/* Missing Skills */}
        <h2>Missing Skills</h2>

        <div className="skills">
          {result.missing_skills.map((skill, index) => (
            <span key={index} className="bad">
              {skill}
            </span>
          ))}
        </div>

        {/* Suggestions */}
        <h2
          style={{
            marginTop: "30px",
            marginBottom: "10px",
          }}
        >
          Suggestions
        </h2>

        {result.ai_generated === true ? (
          <ul
            style={{
              paddingLeft: "22px",
              lineHeight: "1.8",
              marginTop: "0",
            }}
          >
            {result.suggestions.slice(0, 3).map((item, index) => (
              <li key={index}>{item}</li>
          ))}
          </ul>
        ) : (
          <p
            style={{
              color: "#666",
              fontStyle: "italic",
              marginTop: "10px",
              marginBottom: "0",
            }}
          >
            {result.message || "AI suggestions are currently unavailable."}
          </p>
        )}

        <button
          onClick={onReset}
          style={{ marginTop: "25px" }}
        >
          Analyze Another Resume
        </button>
      </div>
    </div>
  );
}

export default Result;