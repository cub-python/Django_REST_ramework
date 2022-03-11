import React from 'react';
import logo from './logo.svg';
import './App.css';
import './bootstrap/css/bootstrap.min.css';
import './bootstrap/css/sticky-footer-navbar.css';
import Footer from './components/Footer.js';
import Navbar from './components/Menu.js';
import UserList from './components/User.js';
import axios from 'axios';
чччччччччччччччччччччччччччччччччччччч
const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            navbarItems: [{name: 'Users', href: '/'},
            ],
            users: []
        }
    }

    componentDidMount() {
        // const users = [
        //     {
        //         'first_name': 'Gottleb',
        //         'last_name': 'Daimler',
        //         'birthday_year': 1834,
        //             'email': 'gdimler@gmail.com'
        //     },
        //     {
        //         'first_name': 'Karl',
        //         'last_name': 'Benz',
        //         'birthday_year': 1864,
        //             'email': 'karl@benz.com'
        //     },
        //     {
        //         'first_name': 'Henry',
        //         'last_name': 'Ford',
        //         'birthday_year': 1863,
        //         'email': 'henry@ford.com'
        //     }
        // ]
        axios.get(get_url('users/'))
            .then(response => {
                this.setState({users: response.data})
            }).catch(error => console.log(error))
    }

    render() {
        return (<div>
                <header>
                    <Navbar navbarItems={this.state.navbarItems}/>
                </header>
                <main role="main" class="flex-shrink-0">
                    <div className="container">
                        <UserList users={this.state.users}/>
                    </div>
                </main>
                <Footer/>
            </div>


        )
    }
}

export default App;
