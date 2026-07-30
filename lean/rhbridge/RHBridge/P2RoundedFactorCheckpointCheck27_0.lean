import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk0 :
    P2RoundedFactorCheckpointData.panel27Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix0_eq :
    P2RoundedFactorCheckpointData.panel27Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk0.1

theorem panel27Prefix1_eq :
    P2RoundedFactorCheckpointData.panel27Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk0.2.1

theorem panel27Prefix2_eq :
    P2RoundedFactorCheckpointData.panel27Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk0.2.2.1

theorem panel27Prefix3_eq :
    P2RoundedFactorCheckpointData.panel27Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk0.2.2.2

end RHP2Bridge
