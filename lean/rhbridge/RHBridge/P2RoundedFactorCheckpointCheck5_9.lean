import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk9 :
    P2RoundedFactorCheckpointData.panel5Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix36_eq :
    P2RoundedFactorCheckpointData.panel5Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk9.1

theorem panel5Prefix37_eq :
    P2RoundedFactorCheckpointData.panel5Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk9.2.1

theorem panel5Prefix38_eq :
    P2RoundedFactorCheckpointData.panel5Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk9.2.2.1

theorem panel5Prefix39_eq :
    P2RoundedFactorCheckpointData.panel5Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk9.2.2.2

end RHP2Bridge
