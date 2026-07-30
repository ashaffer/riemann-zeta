import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk9 :
    P2RoundedFactorCheckpointData.panel15Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix36_eq :
    P2RoundedFactorCheckpointData.panel15Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk9.1

theorem panel15Prefix37_eq :
    P2RoundedFactorCheckpointData.panel15Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk9.2.1

theorem panel15Prefix38_eq :
    P2RoundedFactorCheckpointData.panel15Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk9.2.2.1

theorem panel15Prefix39_eq :
    P2RoundedFactorCheckpointData.panel15Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk9.2.2.2

end RHP2Bridge
