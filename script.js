async function fetchLogs() {
    const res = await fetch("/logs");
    const logs = await res.json();

    console.log("LOGS:", logs);

    const table = document.getElementById("logTable");
    table.innerHTML = "";

    logs.forEach(log => {
        const delay = log.delay || 0;
        const message = log.message || '';
        let rowClass = '';
        if (delay > 1.0) {
            rowClass = 'high-delay';
        } else {
            const keywords = ["hack", "attack", "malware", "Suspicious"];
            for (let keyword of keywords) {
                if (message.toLowerCase().includes(keyword.toLowerCase())) {
                    rowClass = 'alert';
                    break;
                }
            }
        }

        let row = `
        <tr class="${rowClass}">
            <td>${log.time}</td>
            <td>${log.sender}</td>
            <td>${log.receiver}</td>
            <td>${log.message}</td>
            <td>${delay !== null ? delay.toFixed(4) : 'N/A'}</td>
        </tr>`;
        table.innerHTML += row;
    });
}

async function fetchAnalysis() {
    try {
        const res = await fetch("/analyze");
        const analysis = await res.json();

        console.log("ANALYSIS:", analysis);

        document.getElementById("summary").innerHTML = `
            <strong>Summary:</strong> ${analysis.summary.total_logs} logs, 
            ${analysis.summary.high_delays} high delays, 
            ${analysis.summary.suspicious_alerts} alerts
        `;

        const warningsDiv = document.getElementById("warnings");
        warningsDiv.innerHTML = '<h3>Warnings (High Delay >1s):</h3>';
        analysis.warnings.forEach(w => {
            warningsDiv.innerHTML += `<p>${w.message} (from ${w.log.message})</p>`;
        });

        const alertsDiv = document.getElementById("alerts");
        alertsDiv.innerHTML = '<h3>Alerts (Suspicious Keywords):</h3>';
        analysis.alerts.forEach(a => {
            alertsDiv.innerHTML += `<p><strong>${a.keyword}</strong> in: ${a.log.message}</p>`;
        });
    } catch (err) {
        console.error("Analysis fetch error:", err);
    }
}

// Initial loads
fetchLogs();
fetchAnalysis();

// Auto-refresh
setInterval(fetchLogs, 2000);
setInterval(fetchAnalysis, 5000);  // Less frequent

