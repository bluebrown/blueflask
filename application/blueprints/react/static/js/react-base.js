$('a.is-marked').attr('class', 'navbar-item is-mark')
$('#react.is-mark').attr('class', 'navbar-item is-mark is-marked')



const e = React.createElement;

class right_col extends React.Component {

  constructor(props) {
    super(props);
    this.state = { visible: true };
  }

  render() {

    if (this.state.visible) {
      return e(
        'div',
        {class: 'notification is-info',
         onclick: () => this.setState({visible: false})},
        'what can i put here?',
      );
    }

  }
}

// Below we find our component-div in the dom and render
// our component inside.
const menu = document.querySelector('#menu');
const main = document.querySelector('#main');
const sidebar = document.querySelector('#sidebar');
ReactDOM.render(e(right_col), sidebar);
