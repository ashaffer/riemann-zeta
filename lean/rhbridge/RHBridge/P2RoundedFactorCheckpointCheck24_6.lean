import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk6 :
    P2RoundedFactorCheckpointData.panel24Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix24_eq :
    P2RoundedFactorCheckpointData.panel24Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk6.1

theorem panel24Prefix25_eq :
    P2RoundedFactorCheckpointData.panel24Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk6.2.1

theorem panel24Prefix26_eq :
    P2RoundedFactorCheckpointData.panel24Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk6.2.2.1

theorem panel24Prefix27_eq :
    P2RoundedFactorCheckpointData.panel24Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk6.2.2.2

end RHP2Bridge
