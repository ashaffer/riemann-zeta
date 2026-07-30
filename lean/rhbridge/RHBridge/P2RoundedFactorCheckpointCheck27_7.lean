import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk7 :
    P2RoundedFactorCheckpointData.panel27Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix28_eq :
    P2RoundedFactorCheckpointData.panel27Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk7.1

theorem panel27Prefix29_eq :
    P2RoundedFactorCheckpointData.panel27Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk7.2.1

theorem panel27Prefix30_eq :
    P2RoundedFactorCheckpointData.panel27Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk7.2.2.1

theorem panel27Prefix31_eq :
    P2RoundedFactorCheckpointData.panel27Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk7.2.2.2

end RHP2Bridge
