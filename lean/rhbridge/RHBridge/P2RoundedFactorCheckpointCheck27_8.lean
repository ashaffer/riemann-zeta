import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk8 :
    P2RoundedFactorCheckpointData.panel27Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix32_eq :
    P2RoundedFactorCheckpointData.panel27Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk8.1

theorem panel27Prefix33_eq :
    P2RoundedFactorCheckpointData.panel27Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk8.2.1

theorem panel27Prefix34_eq :
    P2RoundedFactorCheckpointData.panel27Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk8.2.2.1

theorem panel27Prefix35_eq :
    P2RoundedFactorCheckpointData.panel27Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk8.2.2.2

end RHP2Bridge
