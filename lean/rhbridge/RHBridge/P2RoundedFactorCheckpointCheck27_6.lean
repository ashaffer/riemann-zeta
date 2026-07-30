import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk6 :
    P2RoundedFactorCheckpointData.panel27Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix24_eq :
    P2RoundedFactorCheckpointData.panel27Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk6.1

theorem panel27Prefix25_eq :
    P2RoundedFactorCheckpointData.panel27Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk6.2.1

theorem panel27Prefix26_eq :
    P2RoundedFactorCheckpointData.panel27Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk6.2.2.1

theorem panel27Prefix27_eq :
    P2RoundedFactorCheckpointData.panel27Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk6.2.2.2

end RHP2Bridge
