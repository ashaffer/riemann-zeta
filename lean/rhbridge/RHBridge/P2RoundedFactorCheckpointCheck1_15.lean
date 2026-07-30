import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk15 :
    P2RoundedFactorCheckpointData.panel1Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix60_eq :
    P2RoundedFactorCheckpointData.panel1Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk15.1

theorem panel1Prefix61_eq :
    P2RoundedFactorCheckpointData.panel1Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk15.2.1

theorem panel1Prefix62_eq :
    P2RoundedFactorCheckpointData.panel1Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk15.2.2.1

theorem panel1Prefix63_eq :
    P2RoundedFactorCheckpointData.panel1Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk15.2.2.2

end RHP2Bridge
