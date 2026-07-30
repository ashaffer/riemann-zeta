import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk15 :
    P2RoundedFactorCheckpointData.panel24Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix60_eq :
    P2RoundedFactorCheckpointData.panel24Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk15.1

theorem panel24Prefix61_eq :
    P2RoundedFactorCheckpointData.panel24Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk15.2.1

theorem panel24Prefix62_eq :
    P2RoundedFactorCheckpointData.panel24Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk15.2.2.1

theorem panel24Prefix63_eq :
    P2RoundedFactorCheckpointData.panel24Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk15.2.2.2

end RHP2Bridge
