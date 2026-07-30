import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk9 :
    P2RoundedFactorCheckpointData.panel17Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Prefix36_eq :
    P2RoundedFactorCheckpointData.panel17Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk9.1

theorem panel17Prefix37_eq :
    P2RoundedFactorCheckpointData.panel17Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk9.2.1

theorem panel17Prefix38_eq :
    P2RoundedFactorCheckpointData.panel17Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk9.2.2.1

theorem panel17Prefix39_eq :
    P2RoundedFactorCheckpointData.panel17Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk9.2.2.2

end RHP2Bridge
