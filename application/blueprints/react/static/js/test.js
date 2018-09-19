// This is a example react component file


const e = React.createElement;
// We do this only for conviennce so we can
// call React.createElement with the variable e.

class LikeButton extends React.Component {
  // This is the real component. It has serveral
  // functions to cunstruct and change its state.

  constructor(props) {
    // we initailize the component in the constructor.
    super(props);
    this.state = { liked: false };
  }

  render() {
  // The render function is responsible for
  // the apearence of our component based on its state.
    if (this.state.liked) {
      return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Like'
    ); // Note that e is React.createElement as metioned above.
  }
}

// Below we find our component-div in the dom and render
// our component inside.
const domContainer = document.querySelector('#react-component');
ReactDOM.render(e(LikeButton), domContainer);
