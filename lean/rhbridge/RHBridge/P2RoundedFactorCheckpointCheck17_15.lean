import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk15 :
    P2RoundedFactorCheckpointData.panel17Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Prefix60_eq :
    P2RoundedFactorCheckpointData.panel17Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk15.1

theorem panel17Prefix61_eq :
    P2RoundedFactorCheckpointData.panel17Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk15.2.1

theorem panel17Prefix62_eq :
    P2RoundedFactorCheckpointData.panel17Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk15.2.2.1

theorem panel17Prefix63_eq :
    P2RoundedFactorCheckpointData.panel17Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk15.2.2.2

end RHP2Bridge
