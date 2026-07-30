import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk6 :
    P2RoundedFactorCheckpointData.panel15Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix24_eq :
    P2RoundedFactorCheckpointData.panel15Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk6.1

theorem panel15Prefix25_eq :
    P2RoundedFactorCheckpointData.panel15Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk6.2.1

theorem panel15Prefix26_eq :
    P2RoundedFactorCheckpointData.panel15Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk6.2.2.1

theorem panel15Prefix27_eq :
    P2RoundedFactorCheckpointData.panel15Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk6.2.2.2

end RHP2Bridge
