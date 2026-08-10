import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);


class Terminal {

    constructor(userChoice) {

        this.rootDir = path.join(__dirname, "..", "data");

        try {

            this.commandList = {

                "help": () => this.help(),

                "ls": () => this.ls(),
                "mkdir": () => this.mkdir(),
                "touch": () => this.touch(),
                "rm": () => this.rm(),
                "cat": () => this.cat(),
                "nano": () => this.nano(),

                "clear": () => this.clear(),
                "cls": () => this.clear(),

                "uptime": () => this.uptime(),
                "sysinfo": () => this.sysinfo(),
                "sysabout": () => this.sysabout(),

                "exit": () => this.exit(),

            };

            this.startTime = Date.now();

            if (userChoice) {
                this.commandList[userChoice]();
            };

        }

        catch (e) {
            console.log(`Unknown [${userChoice}] command. Type [help] for all listed commands`);
        };

    };

    help() {

        console.log("\nAvailable Commands:");

        console.log("\n[ls] use to see inside directory");
        console.log("[mkdir] use to create a folder");
        console.log("[touch] use to create a file");
        console.log("[rm] use to delete a file");
        console.log("[cat] use to print info inside file")
        console.log("[nano] use to create a file and open inside editor");

        console.log("\n[clear] use to clear terminal");
        console.log("[uptime] use to check current time");

        console.log("\n[syslogs] use to check logs")
        console.log("[sysinfo] use to see about system information");
        console.log("[sysabout] use to check about system about ");

        console.log("\nType `exit` to exit the terminal");
    };

    ls() {

        let files = fs.readdirSync("./os/data");

        files.forEach(element => {
            console.log(`- ${element}`);
        });
    };

    mkdir(folderName) {

        const folderPath = path.join(this.rootDir, folderName);

        if (fs.existsSync(folderPath)) {
            console.log(`Folder [${folderName}] already exists.`);
            return;
        }

        fs.mkdirSync(folderPath, { recursive: true });
        console.log(`Folder [${folderName}] created.`);

    };

    touch(fileName) {
        
        const filePath = path.join(this.rootDir, fileName);

        if (fs.existsSync(filePath)) {
            console.log("File already exists.");
            return;
        }

        fs.closeSync(fs.openSync(filePath, "a"));
        console.log(`File [${fileName}] created.`);
    }

    rm(fileName) {

        const filePath = path.join(this.rootDir, fileName);

        if (!fs.existsSync(filePath)) {
            console.log(`File [${fileName}] does not exist.`);
            return;
        }

        fs.unlinkSync(filePath);
        console.log(`File [${fileName}] removed.`);
    }

    cat(fileName) {

        const filePath = path.join(this.rootDir, fileName);

        if (!fs.existsSync(filePath)) {
            console.log(`File [${fileName}] does not exist.`);
            return;
        }

        console.log(fs.readFileSync(filePath, "utf8"));
    }

    nano(fileName, content) {

        const filePath = path.join(this.rootDir, fileName);

        fs.writeFileSync(filePath, content || "");
        console.log(`File [${fileName}] saved.`);
    }

    clear() {
        console.clear();
    };

    uptime() {

        this.uptimeInterval = setInterval(() => {
            const elapsedMilliseconds = Date.now() - this.startTime;
            const uptimeSeconds = Math.floor(elapsedMilliseconds / 1000);

            const hours = Math.floor(uptimeSeconds / 3600);
            const minutes = Math.floor((uptimeSeconds % 3600) / 60);
            const seconds = uptimeSeconds % 60;

            console.clear();
            console.log(`System uptime: ${hours}h ${minutes}m ${seconds}s`);
        }, 1000);
    };

    sysinfo() {

        console.log("\n============================");
        console.log("=========[About OS]=========");
        console.log("============================");

        console.log("Built using JavaScript");
        console.log("[Version]: 1.0.0");
        console.log("[Architecture]: Modular CLI System");
        console.log("\nModules:");
        console.log("- File system");
        console.log("- Folder Manager");
        console.log("- Memory Manager");
        console.log("- Process Manager");
        console.log("- Logs");
        console.log("- Command Terminal");
        console.log("============================");
    };

    sysabout() {

        console.log("\n=====================================");
        console.log("=========[System Information]=========");
        console.log("=======================================");

        console.log("Built using JavaScript");
        console.log("[OS NAME]: JS OS Simulator");
        console.log("[Version]: 1.0.0");
        console.log("[Language]: JavaScript");
        console.log("\nModules Loaded:");
        console.log("- File system");
        console.log("- Folder Manager");
        console.log("- Memory Manager");
        console.log("- Process Manager");
        console.log("- Logs");
        console.log("- Command Terminal");
        console.log("=======================================");
    };

    exit() {

        if (this.uptimeInterval) {
            clearInterval(this.uptimeInterval);
        };

        console.log("Terminal exited.");
    };

}


let term = new Terminal();

term.touch("test.txt");
term.mkdir("state");
term.nano("file.txt", "Hello");
term.cat("file.txt");
term.rm("file.txt");