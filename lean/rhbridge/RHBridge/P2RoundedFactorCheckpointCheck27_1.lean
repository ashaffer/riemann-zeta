import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk1 :
    P2RoundedFactorCheckpointData.panel27Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix4_eq :
    P2RoundedFactorCheckpointData.panel27Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk1.1

theorem panel27Prefix5_eq :
    P2RoundedFactorCheckpointData.panel27Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk1.2.1

theorem panel27Prefix6_eq :
    P2RoundedFactorCheckpointData.panel27Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk1.2.2.1

theorem panel27Prefix7_eq :
    P2RoundedFactorCheckpointData.panel27Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk1.2.2.2

end RHP2Bridge
