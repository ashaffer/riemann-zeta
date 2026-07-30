import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk4 :
    P2RoundedFactorCheckpointData.panel27Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix16_eq :
    P2RoundedFactorCheckpointData.panel27Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk4.1

theorem panel27Prefix17_eq :
    P2RoundedFactorCheckpointData.panel27Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk4.2.1

theorem panel27Prefix18_eq :
    P2RoundedFactorCheckpointData.panel27Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk4.2.2.1

theorem panel27Prefix19_eq :
    P2RoundedFactorCheckpointData.panel27Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk4.2.2.2

end RHP2Bridge
