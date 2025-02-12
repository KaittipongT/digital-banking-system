import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <nav className="bg-blue-600 text-white p-4 flex justify-between">
            <h1 className="text-xl font-bold">Digital Bank</h1>
            <div>
                <Link to="/dashboard" className="mr-4">Dashboard</Link>
                <Link to="/accounts" className="mr-4">Accounts</Link>
                <Link to="/transactions">Transactions</Link>
            </div>
        </nav>
    );
};

export default Navbar;
