import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk13 :
    P2RoundedFactorCheckpointData.panel27Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix52_eq :
    P2RoundedFactorCheckpointData.panel27Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk13.1

theorem panel27Prefix53_eq :
    P2RoundedFactorCheckpointData.panel27Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk13.2.1

theorem panel27Prefix54_eq :
    P2RoundedFactorCheckpointData.panel27Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk13.2.2.1

theorem panel27Prefix55_eq :
    P2RoundedFactorCheckpointData.panel27Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk13.2.2.2

end RHP2Bridge
