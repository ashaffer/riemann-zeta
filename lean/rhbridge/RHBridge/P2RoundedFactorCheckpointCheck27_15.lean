import RHBridge.P2RoundedFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FactorChunk15 :
    P2RoundedFactorCheckpointData.panel27Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨27, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel27Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨27, by decide⟩ := by
  decide +kernel

theorem panel27Prefix60_eq :
    P2RoundedFactorCheckpointData.panel27Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk15.1

theorem panel27Prefix61_eq :
    P2RoundedFactorCheckpointData.panel27Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk15.2.1

theorem panel27Prefix62_eq :
    P2RoundedFactorCheckpointData.panel27Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk15.2.2.1

theorem panel27Prefix63_eq :
    P2RoundedFactorCheckpointData.panel27Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨27, by decide⟩ := by
  exact panel27FactorChunk15.2.2.2

end RHP2Bridge
