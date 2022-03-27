import React from 'react';
import axios from "axios";
import logo from './logo.svg';
import {HashRouter, Route, BrowserRouter, Link, Switch,Redirect}
from "react-router-dom";
import './bootstrap/css/bootstrap.min.css'
import './bootstrap/css/sticky-footer-navbar.css'
import Footer from './components/Footer.js'
import Navbar from './components/Menu.js'
import UserList from './components/User.js'
import {ProjectList, ProjectDetail} from './components/Project.js'
import ToDoList from './components/ToDo.js'
import LoginForm from './components/Auth.js'
import Cookies from 'universal-cookie';
import Nav from 'react-bootstrap/Nav';


import NotFound404 from "./components/NotFound404.js";

const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            // navbarItems: [
            //     {name: 'Users', href: '/'},
            //     {name: 'Projects', href: '/projects'},
            //     {name: 'TODOs', href: '/todos'},
            // ],
            users: [],
            projects: [],
            project: {},
            todos: [],
            'token': "",
            // auth: {username: '', is_login: false}
        }
    }
       set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

        get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const usersDRF = response.data
                this.setState(
                    {
                        'usersDRF': usersDRF
                    }
                );
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                const project = response.data.results
                this.setState(
                    {
                        'projects': project
                    }
                );
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/', {headers})
            .then(response => {
                const todo = response.data.results
                this.setState(
                    {
                        'todos': todo
                    }
                );
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
    }


    render() {
        return (
            <div className="App">
                <BrowserRouter>
                    <Navbar bg="light" expand="lg">
                        <Container>
                            <Navbar.Collapse id="basic-navbar-nav">
                                <Nav className="me-auto">
                                    <Nav.Link><Link to='/'>Home </Link></Nav.Link>
                                    <Nav.Link><Link to='/users'>Users</Link></Nav.Link>
                                    <Nav.Link><Link to='/projects'>Projects</Link></Nav.Link>
                                    <Nav.Link><Link to='/todos'>ToDo</Link></Nav.Link>

                                    <Nav.Link>
                                        <li>
                                            {this.is_authenticated() ?
                                                <button onClick={() => this.logout()}>Logout</button> :
                                                <Link to='/login'>Login</Link>}
                                        </li>

                                    </Nav.Link>
                                </Nav>
                            </Navbar.Collapse>
                        </Container>
                    </Navbar>
                    <Routes>
                        <Route path='/'/>
                        <Route path='/users' element={<UserList users={this.state.users}/>}/>

                        <Route path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route path="/projects/:id" element={<ProjectUser projects={this.state.projects}/>}/>

                        <Route path='/todos' element={<ToDoList todos={this.state.todos}/>}/>

                        <Route path='/login' element={<LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>

                        <Route path="*" element={<NotFound404/>}/>
                    </Routes>
                </BrowserRouter>
                <Footer/>
            </div>
        )
    }
}

export default App;