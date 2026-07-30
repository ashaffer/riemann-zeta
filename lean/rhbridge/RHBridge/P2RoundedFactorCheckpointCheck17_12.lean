import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk12 :
    P2RoundedFactorCheckpointData.panel17Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Prefix48_eq :
    P2RoundedFactorCheckpointData.panel17Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk12.1

theorem panel17Prefix49_eq :
    P2RoundedFactorCheckpointData.panel17Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk12.2.1

theorem panel17Prefix50_eq :
    P2RoundedFactorCheckpointData.panel17Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk12.2.2.1

theorem panel17Prefix51_eq :
    P2RoundedFactorCheckpointData.panel17Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk12.2.2.2

end RHP2Bridge
