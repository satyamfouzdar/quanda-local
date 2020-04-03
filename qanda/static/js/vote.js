let vote = 0;

const increment = () => {
  vote++;
  renderCounterApp();
};

const decrement = () => {
  vote--;
  renderCounterApp();
};

const voteId = document.getElementById('vote');

const renderCounterApp = () => {
  const voteTemplate = /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    className: "row center"
  }, /*#__PURE__*/React.createElement("i", {
    id: "increment",
    className: "fas fa-4x fa-sort-up",
    onClick: increment
  })), /*#__PURE__*/React.createElement("div", {
    className: "row pr-2"
  }, /*#__PURE__*/React.createElement("div", {
    className: "container"
  }, vote)), /*#__PURE__*/React.createElement("div", {
    className: "row center"
  }, /*#__PURE__*/React.createElement("i", {
    id: "decrement",
    className: "fas fa-4x fa-sort-down",
    onClick: decrement
  })));
  ReactDOM.render(voteTemplate, voteId);
};

renderCounterApp();
