import { useState } from "react";
import Home from "./Home";
import Loading from "./Loading";
import Result from "./Result";

function App() {
  const [page, setPage] = useState("home");
  const [result, setResult] = useState(null);

  const startLoading = () => {
    setPage("loading");
  };

  const showResult = (data) => {
    setResult(data);
    setPage("result");
  };

  const handleReset = () => {
    setResult(null);
    setPage("home");
  };

  if (page === "home") {
    return (
      <Home
        startLoading={startLoading}
        showResult={showResult}
      />
    );
  }

  if (page === "loading") {
    return <Loading />;
  }

  return (
    <Result
      result={result}
      onReset={handleReset}
    />
  );
}

export default App;