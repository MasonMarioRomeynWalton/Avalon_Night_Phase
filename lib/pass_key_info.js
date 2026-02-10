const pass_key = window.sessionStorage.getItem("avalon_pass");
fetch("info?pass_key=" + pass_key)
    .then( response => response.text() )
    .then( result => {
        let parser = new DOMParser();
        doc = parser.parseFromString( result, 'text/html' );
        document.replaceChild( doc.documentElement, document.documentElement );
    } );
