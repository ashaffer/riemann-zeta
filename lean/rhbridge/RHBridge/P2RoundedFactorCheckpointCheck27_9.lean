import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk9 :
    P2RoundedFactorCheckpointData.panel27Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix36_eq :
    P2RoundedFactorCheckpointData.panel27Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk9.1

theorem panel27Prefix37_eq :
    P2RoundedFactorCheckpointData.panel27Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk9.2.1

theorem panel27Prefix38_eq :
    P2RoundedFactorCheckpointData.panel27Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk9.2.2.1

theorem panel27Prefix39_eq :
    P2RoundedFactorCheckpointData.panel27Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk9.2.2.2

end RHP2Bridge
