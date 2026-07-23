import { useState } from "react";
import axios from "axios";
import "./index.css";

function Home({ startLoading, showResult }) {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");

  const handleSubmit = async () => {
    if (!resume) {
      alert("Please upload a resume.");
      return;
    }

    if (!jobDescription.trim()) {
      alert("Please enter a job description.");
      return;
    }

    // Show loading page immediately
    startLoading();

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/analyze",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      showResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to analyze resume.");

      // Return to home page if request fails
      window.location.reload();
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h1>AI ATS Resume Analyzer</h1>

        <p className="subtitle">
          Upload your resume and compare it with a job description.
        </p>

        <label className="label">Upload Resume (PDF)</label>

        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setResume(e.target.files[0])}
        />

        <label className="label">Job Description</label>

        <textarea
          placeholder="Paste the job description here..."
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        ></textarea>

        <button onClick={handleSubmit}>
          Analyze Resume
        </button>
      </div>
    </div>
  );
}

export default Home;