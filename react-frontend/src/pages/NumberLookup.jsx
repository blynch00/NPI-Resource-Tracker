import { SearchForm } from "../components/SearchForm"

export function NumberLookup(){
    return (
            <div className="container">
                <header className="page-header">
                    <h1>NPI Lookup</h1>
                </header>
                <div className="page-content">
                    <SearchForm/>
                </div>
            </div>
            
        );
    }