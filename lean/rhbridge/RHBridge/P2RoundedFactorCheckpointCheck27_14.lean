import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk14 :
    P2RoundedFactorCheckpointData.panel27Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix56_eq :
    P2RoundedFactorCheckpointData.panel27Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk14.1

theorem panel27Prefix57_eq :
    P2RoundedFactorCheckpointData.panel27Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk14.2.1

theorem panel27Prefix58_eq :
    P2RoundedFactorCheckpointData.panel27Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk14.2.2.1

theorem panel27Prefix59_eq :
    P2RoundedFactorCheckpointData.panel27Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk14.2.2.2

end RHP2Bridge
