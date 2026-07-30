import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk5 :
    P2RoundedFactorCheckpointData.panel27Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix20_eq :
    P2RoundedFactorCheckpointData.panel27Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk5.1

theorem panel27Prefix21_eq :
    P2RoundedFactorCheckpointData.panel27Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk5.2.1

theorem panel27Prefix22_eq :
    P2RoundedFactorCheckpointData.panel27Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk5.2.2.1

theorem panel27Prefix23_eq :
    P2RoundedFactorCheckpointData.panel27Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk5.2.2.2

end RHP2Bridge
