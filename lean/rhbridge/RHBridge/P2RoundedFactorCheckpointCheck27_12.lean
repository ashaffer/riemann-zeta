import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk12 :
    P2RoundedFactorCheckpointData.panel27Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix48_eq :
    P2RoundedFactorCheckpointData.panel27Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk12.1

theorem panel27Prefix49_eq :
    P2RoundedFactorCheckpointData.panel27Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk12.2.1

theorem panel27Prefix50_eq :
    P2RoundedFactorCheckpointData.panel27Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk12.2.2.1

theorem panel27Prefix51_eq :
    P2RoundedFactorCheckpointData.panel27Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk12.2.2.2

end RHP2Bridge
