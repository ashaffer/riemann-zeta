import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk6 :
    P2RoundedFactorCheckpointData.panel10Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Prefix24_eq :
    P2RoundedFactorCheckpointData.panel10Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk6.1

theorem panel10Prefix25_eq :
    P2RoundedFactorCheckpointData.panel10Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk6.2.1

theorem panel10Prefix26_eq :
    P2RoundedFactorCheckpointData.panel10Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk6.2.2.1

theorem panel10Prefix27_eq :
    P2RoundedFactorCheckpointData.panel10Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk6.2.2.2

end RHP2Bridge
