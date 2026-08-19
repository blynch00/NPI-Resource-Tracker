

export function SearchForm() {
    return (
        <form className="search-form">
            <div className="form-row">
                <label htmlFor="npi">NPI</label>
                <input
                    id="npi"
                    name="npi"
                    type="text"
                    placeholder="Enter NPI"
                />
            </div>

            <div className="form-row">
                <label htmlFor="firstName">First Name</label>
                <input
                    id="firstName"
                    name="firstName"
                    type="text"
                    placeholder="Enter first name"
                />
            </div>

            <div className="form-row">
                <label htmlFor="lastName">Last Name</label>
                <input
                    id="lastName"
                    name="lastName"
                    type="text"
                    placeholder="Enter last name"
                />
            </div>

            <div className="form-row">
                <label htmlFor="state">State</label>
                <input
                    id="state"
                    name="state"
                    type="text"
                    placeholder="Enter state"
                />
            </div>

            <button type="submit">
                Search
            </button>
        </form>
    );
}