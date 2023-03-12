import React from 'react'
import {Container, Navbar} from "react-bootstrap"

export default function Menu2()
{
    return (
        <header>
            <Navbar bg="dark" variant="dark" expand="lg">
                <Container>
                    <Navbar.Brand href="#home">React Rest Django</Navbar.Brand>
                </Container>
            </Navbar>
        </header>
    )
}