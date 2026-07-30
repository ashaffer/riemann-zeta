import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk11 :
    P2RoundedFactorCheckpointData.panel27Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix44_eq :
    P2RoundedFactorCheckpointData.panel27Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk11.1

theorem panel27Prefix45_eq :
    P2RoundedFactorCheckpointData.panel27Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk11.2.1

theorem panel27Prefix46_eq :
    P2RoundedFactorCheckpointData.panel27Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk11.2.2.1

theorem panel27Prefix47_eq :
    P2RoundedFactorCheckpointData.panel27Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk11.2.2.2

end RHP2Bridge
