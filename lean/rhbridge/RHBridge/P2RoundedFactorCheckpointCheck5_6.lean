import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk6 :
    P2RoundedFactorCheckpointData.panel5Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix24_eq :
    P2RoundedFactorCheckpointData.panel5Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk6.1

theorem panel5Prefix25_eq :
    P2RoundedFactorCheckpointData.panel5Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk6.2.1

theorem panel5Prefix26_eq :
    P2RoundedFactorCheckpointData.panel5Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk6.2.2.1

theorem panel5Prefix27_eq :
    P2RoundedFactorCheckpointData.panel5Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk6.2.2.2

end RHP2Bridge
